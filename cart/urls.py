from .views import MyCart , CheckOut , IncreaseQty , DecreaseQty , AddProduct , DeleteItem , OrderDetail
from django.urls import path

urlpatterns = [
    path("" , MyCart , name = 'cart'),
    path("checkout/" , CheckOut , name = 'checkout'),
    path("checkout/" , CheckOut , name = 'checkout'),
    path("order-detail/<str:id>/" , OrderDetail , name = 'order-detail'),

    # Increasing qty method url
    path("increase/<str:id>/" , IncreaseQty , name = 'increase'),
    path("decrease/<str:id>/" , DecreaseQty , name = 'decrease'),
    path("delete/<str:id>/" , DeleteItem , name = 'delete-item'),

]
