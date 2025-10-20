from product.models import Category
from .models import Cart , CartItem

def CategoryList(request):
    categories = Category.objects.all()
    return {"categories":categories}

def TotalItem(request):
    total = CartItem.objects.filter(cart = request.cart).count()
    return {"total":total}