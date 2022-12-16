from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store.views import index, product_detail
from accounts.views import signup
from shop import settings

urlpatterns = [
                  path('', index, name='index'),
                  path('admin/', admin.site.urls),
                  path('product/<str:slug>/', product_detail, name="product"),
                  path('signup/', signup, name="sign up"),
                  # path('product/<str:slug>/add-to-cart/', add_to_cart, name = "add-to-cart")

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
