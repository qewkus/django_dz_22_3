from catalog.forms import ProductForm
from catalog.models import Product
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin)



class CatalogHomeView(ListView):
    model = Product
    template_name = "catalog/base.html"
    context_object_name = "products"


class CatalogContactsView(View):
    def get(self, request):
        return render(request, "catalog/contacts.html")

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо,{name}, ваше сообщение получено!")


class CatalogDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.filter(published=True)
    template_name = "index.html"
    context_object_name = "products"
    paginate_by = 20


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_create.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_create.html"
    success_url = reverse_lazy("catalog:home")

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("catalog:home")

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        # Удалять может владелец или модератор (пользователь с правом delete_product)
        return product.owner == user or user.has_perm("catalog.delete_product")


class ContactsView(TemplateView):
    template_name = "contacts.html"
