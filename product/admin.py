from django.contrib import admin
from .models import  Category , Product
# Register your models here


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name" , 'price' , "stock" , "unit" , "is_active" , "date"]

@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ["name" , 'is_active' , 'date' ]
