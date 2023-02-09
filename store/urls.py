from django.urls import path
from store.views import store,cart,checkout,home

urlpatterns = [

    path("",home,name='home'),
    path("store/",store,name='store'),
    path("cart/",cart,name='cart'),
    path("checkout/",checkout,name='checkout'),

]