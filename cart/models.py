from django.db import models
import uuid
from session.models import CustomUser
from django.utils.timezone import now
from product.models import Product
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
    date = models.DateField(default = now)

    class Meta:
        ordering = ["cart" , "-date"]


