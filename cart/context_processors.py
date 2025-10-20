from product.models import Category
from .models import Cart , CartItem

def CategoryList(request):
    categories = Category.objects.all()
    return {"categories":categories}
