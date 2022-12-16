from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from store.models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', context={"products": products})


# afficher détails de chaque produit :
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'detail.html', context={"product": product})


def add_to_cart(request):
    pass
