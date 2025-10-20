
from django.contrib import admin
from django.urls import path , include
from product.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home , name = 'home'),
    path('product/', include('product.urls')),
    path('session/', include('session.urls')),
    path('cart/', include('cart.urls')),
    path('summernote/', include('django_summernote.urls')),
]
