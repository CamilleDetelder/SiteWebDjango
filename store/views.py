
from django.shortcuts import render

from store.models import Product


# Create your views here.
def index(request):
    Product.objects.all()
    return render(request, "index.html",)

def add_to_cart(request):
    pass

