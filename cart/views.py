from django.shortcuts import render , HttpResponse , redirect
from .models import CartItem
from functools import wraps
from django.contrib import messages
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

def MyCart(request):
    items = CartItem.objects.filter(cart = request.cart , is_ordered = False)
    price = sum(item.price for item in items)
    return render(request , 'cart.html' , {"items":items , "price":price})

def CheckOut(request):
    items = CartItem.objects.filter(cart = request.cart , is_ordered = False)
    price = sum(item.price for item in items)
    return render(request , 'checkout.html' , {"items":items , "price":price})

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
        messages.success(request , f'{qty} {product.unit} { product.name} added toy your cart')

        REFERER = request.META.get('HTTP_REFERER' , '/shop')
        return redirect(REFERER)

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
        messages.success(request , f"1 {item.product.unit} {item.product} added to your cart")
    return redirect('cart')

@itemRequired
def DeleteItem(request , id , item):
    messages.success(request , f'{item.product} deleted')
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
        messages.success(request , f"1 {item.product.unit} {item.product} deleted to your cart")
    else:
        messages.success(request, f'{item.product} deleted')
        item.product.stock += 1
        item.product.save()
        item.delete()
    return redirect('cart')
