from django.contrib import admin
from .models import Cart , CartItem , ConfirmOrder
# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user"]

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["cart" , "product" , "qty" , "price" , "is_ordered"]

@admin.register(ConfirmOrder)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["name","phone","email","location","shipping_charge","price","status"]
