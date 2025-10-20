from django.shortcuts import render

# Create your views here.

def Home(request):
    print(request.cart)
    return render(request , 'index.html')

def Shop(request):
    return render(request , 'shop.html')