from django.shortcuts import render , get_object_or_404
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def Home(request):
    return render(request , 'index.html')

def Shop(request):
    products = Product.objects.all()
    paginator = Paginator(object_list = products , per_page = 20)
    page = request.GET.get("page")
    products = paginator.get_page(page)
    return render(request , 'shop.html' , {"products":products})

def ProductDetail(request , id):
    product = get_object_or_404(Product , id = id)
    return render(request , 'product.html' , {"product":product})