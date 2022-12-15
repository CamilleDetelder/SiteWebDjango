
from django.contrib import admin
from django.urls import path
from store.views import index, add_to_cart
from accounts.views import signup

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name="sign up"),
    # path('product/<str:slug>/add-to-cart/', add_to_cart, name = "add-to-cart")
    # faire url pour panier
]
