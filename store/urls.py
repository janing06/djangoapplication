from django.urls import path
from store.views import store,cart,checkout,home,removal

urlpatterns = [

    path("",home,name='home'),
    path("store/",store,name='store'),
    path("removal/",removal,name='removal'),
    path("cart/",cart,name='cart'),
    path("checkout/",checkout,name='checkout'),

]