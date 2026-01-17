from catalog.apps import CatalogConfig
from catalog.views import (
    CatalogContactsView,
    CatalogDetailView,
    CatalogHomeView,
    ProductCreateView,
    ProductDeleteView,
    ProductUpdateView,
)
from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.ProductListView.as_view(), name="index"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path(
        "products/<int:pk>/",
        cache_page(60)(views.ProductDetailView.as_view()),
        name="product_details",
    ),
    path("products/create/", views.ProductCreateView.as_view(), name="product_create"),
    path(
        "products/update/<int:pk>/",
        views.ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "products/delete/<int:pk>/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path(
        "category/<int:pk>/",
        views.CategoryProductListView.as_view(),
        name="category_products",
    ),
]
