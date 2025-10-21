from django.shortcuts import render , HttpResponse , redirect
from .models import Product  , ProductReview
from django.core.paginator import Paginator
from functools import wraps
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm
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
    products = Product.objects.filter(is_active = True)
    paginator = Paginator(object_list = products , per_page = 20)
    page = request.GET.get("page")
    products = paginator.get_page(page)
    return render(request , 'shop.html' , {"products":products})

@ProductRequired
def ProductDetail(request , id , product):
    form = ReviewForm()
    reviews = ProductReview.objects.filter(product = product)
    return render(request , 'product.html' , {"product":product , "reviews":reviews , "form":form})

@login_required
@ProductRequired
def AddReview(request , id , product):
    REFERER = request.META['HTTP_REFERER']
    if request.method == 'POST':
        form = ReviewForm(data = request.POST)
        if form.is_valid():
            review = form.save(commit = False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request , 'Thanks for your review')
        else:
            messages.error(request , 'Something went wrong')

    return redirect(REFERER)
    

