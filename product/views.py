from django.shortcuts import render , HttpResponse , redirect
from .models import Product  , ProductReview
from django.core.paginator import Paginator
from functools import wraps
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm , RequestForm
from django.core.mail import send_mail
from session.views import get_user
from django.db.models import Q
# Create your views here.

def ProductRequired(func):
    @wraps(func)
    def wrapper(request , id , *args , **kwargs):
        try:
            product = Product.objects.get(id = id)
        except Product.DoesNotExist:
            return HttpResponse(content = "Product not found")
        return func(request , id , product , *args , **kwargs)
    return wrapper

def Home(request):
    return render(request , 'index.html')

def Shop(request):
    products = Product.objects.all()

    # Filtering
    name = request.GET.get("name")
    if name:
        products = products.filter(Q(name__icontains = name))
    paginator = Paginator(object_list = products , per_page = 12)
    page = int(request.GET.get("page" ,  1))
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

@ProductRequired
def Request(request , id , product):
    user = get_user(request)
    if product.stock > 0:
        messages.info(request , "The product is in stock")
        return redirect("product-detail",product.id)
    if request.method == 'POST':
        form = RequestForm(data = request.POST)
        user = get_user(request)

        if form.is_valid():
            new_request = form.save(commit = False)
            if user:
                new_request.user = user
            else:
                name = form.cleaned_data.get("name")
                email = form.cleaned_data.get("email")
                new_request.name = name
                new_request.email = email
            new_request.product = product
            new_request.save()
            messages.success(request , "Thanks for request us")
            return redirect("shop")

    else:
        form = RequestForm(initial = {"name":request.user.get_full_name(),"email":request.user.email} if request.user.is_authenticated else None)
    return render(request , "request.html" , {"form":form , "product":product})




    

