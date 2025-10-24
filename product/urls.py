from .views import Shop , ProductDetail , AddReview , Request
from django.urls import path

urlpatterns = [
    path('shop/' , Shop , name = 'shop'),
    path('detail/<str:id>/' , ProductDetail , name = 'product-detail'),

    path('review/<str:id>/' , AddReview , name = 'add-review'),
    path('request/<str:id>/' , Request , name = 'request-product'),
]
