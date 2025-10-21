from .views import MyCart , CheckOut , IncreaseQty , DecreaseQty , AddProduct , DeleteItem
from django.urls import path

urlpatterns = [
    path("" , MyCart , name = 'cart'),
    path("checkout/" , CheckOut , name = 'checkout'),
    path("add/<str:id>/" , AddProduct , name = 'add-product'),

    # Increasing qty method url
    path("increase/<str:id>/" , IncreaseQty , name = 'increase'),
    path("decrease/<str:id>/" , DecreaseQty , name = 'decrease'),
    path("delete/<str:id>/" , DeleteItem , name = 'delete-item'),

]
