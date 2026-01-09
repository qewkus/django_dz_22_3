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

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", CatalogHomeView.as_view(), name="home"),
    path("contacts/", CatalogContactsView.as_view(), name="contacts"),
    path("product_detail/<int:pk>/", CatalogDetailView.as_view(), name="product_detail"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_update/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product_delete/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
]
