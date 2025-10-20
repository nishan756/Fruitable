from .views import Login , LogOut , SignUp
from django.urls import path

urlpatterns = [
    path('login/' , Login , name = 'login'),
    path('signup/' , SignUp , name = 'signup'),
    path('logout/' , LogOut , name = 'logout'),
]
