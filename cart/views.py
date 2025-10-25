from django.shortcuts import render , HttpResponse , redirect
from .models import CartItem , ConfirmOrder
from functools import wraps
from django.contrib import messages
from .forms import OrderForm
from product.views import ProductRequired
# Create your views here.

def itemRequired(func):
    @wraps(func)
    def wrapper(request , id , *args , **kwargs):
        try:
            item = CartItem.objects.get(id = id , cart = request.cart , is_ordered = False)
        except CartItem.DoesNotExist:
            return HttpResponse(content = 'Cart item not found')
        return func(request , id , item , *args , **kwargs)
    return wrapper

def orderRequired(func):
    @wraps(func)
    def wrapper(request , id):
        try:
            order = ConfirmOrder.objects.get(id = id)
        except ConfirmOrder.DoesNotExist:
            return HttpResponse("Order not found")
        return func(request,id,order)
    return wrapper

def MyCart(request):
    items = CartItem.objects.filter(cart = request.cart , is_ordered = False)
    price = sum(item.price for item in items)
    return render(request , 'cart.html' , {"items":items , "price":price})


@ProductRequired
def AddProduct(request , id , product):
    qty = int(request.POST.get('qty' , 1))
    if product.stock >= 1 and qty <= product.stock:
        try:
            cart_item = CartItem.objects.get(is_ordered = False , product = product , cart = request.cart)
        except CartItem.DoesNotExist:
            cart_item = None
        if cart_item:
            cart_item.qty += qty
            cart_item.price = int(cart_item.product.price)*(cart_item.qty)
            cart_item.save()
        else:
            new_item = CartItem.objects.create(
                product = product,
                cart = request.cart,
                qty = qty,
                price = int(product.price)*qty,
            )
            new_item.save()
        product.stock -= qty
        product.save()
        messages.success(request , f'{ product.name} added toy your cart')

        REFERER = request.META.get('HTTP_REFERER' , '/shop')
        return redirect(REFERER)
    else:
        messages.info(request , "Stock Out")

@itemRequired
def IncreaseQty(request , id, item):
    if item.product.stock <= 0:
        messages.info(request , 'Stock Out')
    else:
        item.qty += 1
        item.price += item.product.price
        item.product.stock -= 1
        item.product.save()
        item.save()
        messages.success(request , f"{item.product} added to your cart")
    return redirect('cart')

@itemRequired
def DeleteItem(request , id , item):
    messages.success(request , f'{item.product} deleted')
    item.product.stock += item.qty
    item.product.save()
    item.delete()
    return redirect('cart')

@itemRequired
def DecreaseQty(request , id, item):
    if item.qty > 1:
        item.qty -= 1
        item.price -= item.product.price
        item.product.stock += 1
        item.product.save()
        item.save()
        messages.success(request , f"{item.product} deleted to your cart")
    else:
        messages.success(request, f'{item.product} deleted')
        item.product.stock += 1
        item.product.save()
        item.delete()
    return redirect('cart')

def CheckOut(request):
    items = CartItem.objects.filter(cart = request.cart , is_ordered = False)
    price = sum(item.price for item in items)

    if request.method == "POST":
        form = OrderForm(data = request.POST)
        if form.is_valid():
            order = form.save(commit = False)
            order.cart = request.cart
            order.price  = price + order.shipping_charge.charge
            order.save()
            order.items.set(items)
            order.save()
            messages.success(request , "Thanks for your order")
            return redirect("order-detail",order.id)
        else:
            messages.error(request , "Please correct the errors below")
    else:
        form = OrderForm(initial = {"name":request.user.get_full_name(),"phone":request.user.phone,"email":request.user.email} if request.user.is_authenticated else None)
    return render(request , "checkout.html" , {"form":form,"items":items,"price":price})

@orderRequired
def OrderDetail(request , id , order):
    return render(request , "order-detail.html",{"order":order})