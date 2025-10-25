from django.shortcuts import render
from .models import AboutShop
from .forms import ContactForm
# Create your views here.

def Conditions(request):
    return render(request , "conditions.html")

def Contact(request):
    if request.method == 'POST':
        pass
    else:
        form = ContactForm()
    return render(request , "contact.html" , {"form":form})
