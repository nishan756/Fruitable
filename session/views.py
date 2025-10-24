from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages
from .forms import CustomUserForm
from functools import wraps
# Create your views here.

def get_user(request):
        user = None
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        return user

def SignUp(request):
    if request.method == 'POST':
        form = CustomUserForm(data = request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit = False)
            user.set_password(password)
            user.save()
            messages.success(request , 'Account creation successfull. Please login to continue')
            return redirect('login')
        else:
            messages.error(request , 'Please fillup the form correctly')
    form = CustomUserForm()
    return render(request , 'auth.html' , {'form' : form})


def Login(request):
    form = CustomUserForm()
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request , username = username , password = password)
        if user is not None:
            login(request , user)
            messages.success(request , "Login Successfull")
            return redirect('home')
        else:
            messages.error(request , "Invalid username or password")
    return render(request , 'auth.html' , {'form':form})

def LogOut(request):
    logout(request)
    messages.success(request , 'Logout Successfull')
    return redirect('login')

