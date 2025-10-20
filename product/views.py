from django.shortcuts import render , HttpResponse
from .models import Product
from django.core.paginator import Paginator
from functools import wraps
# Create your views here.

def ProductRequired(func):
    @wraps(func)
    def wrapper(request , id , *args , **kwargs):
        try:
            product = Product.objects.get(id = id , is_active = True)
        except Product.DoesNotExist:
            return HttpResponse(content = "Product not found")
        return func(request , id , product , *args , **kwargs)
    return wrapper

def Home(request):
    return render(request , 'index.html')

def Shop(request):
    products = Product.objects.all()
    paginator = Paginator(object_list = products , per_page = 20)
    page = request.GET.get("page")
    products = paginator.get_page(page)
    return render(request , 'shop.html' , {"products":products})

@ProductRequired
def ProductDetail(request , id , product):
    return render(request , 'product.html' , {"product":product})