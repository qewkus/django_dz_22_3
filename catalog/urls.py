from django.urls import path
from catalog.apps import AppNameConfig
from catalog.views import home, contacts
from . import views

app_name = AppNameConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
]
