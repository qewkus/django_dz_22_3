from django.urls import path
from catalog.apps import AppNameConfig
from . import views

app_name = AppNameConfig.name

urlpatterns = [
    path("", views.index, name="index"),
    path('contacts/', views.contacts, name='contacts'),
    path("products/<int:pk>/", views.product_details, name="product_details"),
]
