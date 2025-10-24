from django.contrib import admin
from .models import  Category , Product , ProductReview , ProductRequest
# Register your models here


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name" , 'price' , "stock" , "unit" , "is_active" , "date"]

@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ["name" , 'is_active' , 'date' ]

@admin.register(ProductReview)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user" , "product" , "date"]

@admin.register(ProductRequest)
class RequestAdmin(admin.ModelAdmin):
    list_display = ["user","name","email","product","date"]
    
