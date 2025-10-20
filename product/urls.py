from .views import Shop
from django.urls import path

urlpatterns = [
    path('shop/' , Shop , name = 'shop'),
]
