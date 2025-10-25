from django.contrib import admin
from .models import AboutShop , ShippingCharge , Contact
# Register your models here.

@admin.register(AboutShop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ["name","email","location","established_at"]
    readonly_fields = ["created_at"]

@admin.register(ShippingCharge)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ["area_type","location","charge"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name","email","subject","created_at"]


#----------------------------
about = AboutShop.objects.first()

if about is not None:
    admin.site.site_header = about.name
    admin.site.site_title = about.name

    


