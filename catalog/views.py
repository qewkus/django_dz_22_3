from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory

from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version, Category


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/product.html'

    # def get_queryset(self):
    #     return super().get_queryset().filter(
    #         category=self.kwargs.get('pk'),
    #         owner=self.request.user
    #     )

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     category_item = Category.objects.get(pk=self.kwargs.get('pk'))
    #     context_data['category_pk'] = category_item.pk
    #     context_data['title'] = f'Продукты - вск категории {category_item.name}'
    #     return context_data


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    permission_required = 'catalog.view_product'



class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    success_url = reverse_lazy('catalog:product')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    success_url = reverse_lazy('catalog:product')

    # def get_queryset(self):
    #     queryset = super().get_queryset().filter(
    #         category=self.kwargs.get('pk'),
    #     )
    #     if not self.request.user.is_staff:
    #         queryset = queryset.filter(owner=self.request.user)
    #     return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('catalog:product')


class VersionListView(LoginRequiredMixin, ListView):
    model = Version
    form_class = VersionForm


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
