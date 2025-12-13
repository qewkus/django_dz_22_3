from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, get_object_or_404
from catalog.models import Product


def index(request):
    product_list = Product.objects.all()
    # Pagination with 3 products per page
    paginator = Paginator(product_list, 3)
    page_number = request.GET.get("page", 1)
    products = paginator.page(page_number)

    context = {"products": products}
    return render(request, "index.html", context=context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context=context)


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        return HttpResponse(f'Спасибо, {name}! Сообщение получено')
    return render(request, 'catalog/contacts.html')
