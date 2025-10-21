from django.db import models
import uuid
from cloudinary.models import CloudinaryField
from django.utils.timezone import now
from django_summernote.fields import SummernoteTextField
from django.contrib.auth import get_user_model
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)
    image = CloudinaryField(folder = 'fruitable/category' , blank = True , null = True)
    is_active = models.BooleanField(default = False)
    date = models.DateTimeField(default = now)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-date"]
        verbose_name_plural = 'Categories'


UNIT = [
    ('Kg' , 'Kg'),
    ('Gm' , 'Gm'),
    ('Pcs' , 'Pcs'),
    ('Dozen' , 'Dozen'),
]
class Product(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    name = models.CharField(max_length = 100)
    category = models.ManyToManyField(Category)
    image = CloudinaryField(folder = 'fruitable/product' , blank = True , null = True)
    price = models.DecimalField(decimal_places = 2 , max_digits = 8)
    stock = models.PositiveIntegerField()
    unit = models.CharField(choices = UNIT , default = "Kg")
    is_active = models.BooleanField(default = False)
    description = SummernoteTextField(blank = True)
    date = models.DateTimeField(default = now)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-date"]

User = get_user_model()
class ProductReview(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    product = models.ForeignKey(Product , on_delete = models.CASCADE)
    review = SummernoteTextField()
    date = models.DateTimeField(default = now)

    def __str__(self):
        return f'{self.user.usernae} reviewd a product'
    class Meta:
        ordering = ["-date" , "product"]
        unique_together = ["user" , "product"]








