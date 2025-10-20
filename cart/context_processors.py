from product.models import Category
from .models import Cart , CartItem

def CategoryList(request):
    categories = Category.objects.all(is_active = True)
    return {"categories":categories}

def TotalItem(request):
    total = CartItem.objects.filter(cart = request.cart , is_ordered = False).count()
    return {"total":total}