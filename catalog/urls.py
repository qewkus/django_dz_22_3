from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import AppNameConfig
from catalog.views import ProductListView, ProductCreateView, ProductUpdateView, VersionListView, \
    ProductDelete, ProductDetailView

app_name = AppNameConfig.name

urlpatterns = [
    path('', cache_page(60)(home), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/', ProductListView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('', VersionListView.as_view(), name='list'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='delete_product'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
]
