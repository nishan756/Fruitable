from django.db import models
import uuid
from session.models import CustomUser
from django.utils.timezone import now
from product.models import Product
from about.models import ShippingCharge
# Create your models here.

class Cart(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    session_key = models.CharField(max_length = 100 , blank = True , null = True)
    user = models.OneToOneField(CustomUser , on_delete = models.SET_NULL , blank = True , null = True)
    date = models.DateTimeField(default = now)

    def __str__(self):
        return str(self.user) if self.user else self.session_key
    class Meta:
        ordering = ["-date",]

class CartItem(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    cart = models.ForeignKey(Cart , on_delete = models.SET_NULL , blank = True , null = True)
    product = models.ForeignKey(Product , on_delete = models.SET_NULL , blank = True , null = True)
    qty = models.PositiveIntegerField(default = 1)
    price = models.DecimalField(decimal_places = 2 , max_digits = 8)
    is_ordered = models.BooleanField(default = False)
    date = models.DateField(default = now)

    def __str__(self):
        return f"{self.product} - {self.qty}"

    class Meta:
        ordering = ["cart" , "-date"]
    
STATUS = [
    ("Confirmed","Confirmed"),
    ("Pending","Pending"),
    ("Placed","Placed"),
    ("Cancled","Cancled")
]
class ConfirmOrder(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    cart = models.ForeignKey(Cart , on_delete = models.SET_NULL , blank = True , null = True)
    name = models.CharField(max_length = 200 , blank = True , null = True)
    email = models.EmailField(blank = True , null = True)
    phone = models.CharField(max_length = 11 , blank = True , null = True)
    location = models.CharField(max_length = 300)
    shipping_charge = models.ForeignKey(ShippingCharge , on_delete = models.SET_NULL , blank = True , null = True)
    price = models.DecimalField(decimal_places = 2 , max_digits = 8)
    items = models.ManyToManyField(CartItem)
    status = models.CharField(max_length = 30 , choices = STATUS ,  default = "Pending")
    date = models.DateTimeField(default = now)

    def __str__(self):
        return f'Order confirmed by {self.name} - {self.phone}'
    
    def get_id(self):
        order_id = str(self.id).split('-')[4]
        return order_id
    
    def save(self , *args , **kwargs):
        super().save(*args , **kwargs)
        for item in self.items.all():
            item.is_ordered = True
            item.save()
    
    class Meta:
        ordering = ["-date"]
        verbose_name = "Confirmed Order"
        verbose_name_plural = "Confirmed Orders"

