from django.db import models
from cloudinary.models import CloudinaryField
from django_summernote.fields import SummernoteTextField
from django.utils.timezone import now
import uuid
# Create your models here.

class AboutShop(models.Model):
    name = models.CharField(max_length = 100)
    logo = CloudinaryField(folder = "fruitable/shop_logo" , blank = True , null = True)
    phone = models.CharField(max_length = 110 , help_text = "If you've multiple phone number , separate them via comma(,)")
    location = models.CharField(max_length = 200)
    email = models.EmailField(unique = True)
    terms_and_conditions = SummernoteTextField(blank = True)
    established_at = models.DateField()
    created_at = models.DateTimeField(default = now) 

    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Shop Info"
        verbose_name_plural = verbose_name

class Contact(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    subject = models.CharField(max_length = 200)
    message = SummernoteTextField()
    created_at = models.DateTimeField(default = now)

    def __str__(self):
        return f'{self.name} send a message'

class ShippingCharge(models.Model):
    AREA_TYPE = [
        ('Inside' , 'Inside'),
        ('Outside' , 'Outside'),
    ]
    area_type = models.CharField(max_length = 50 , choices = AREA_TYPE)
    location = models.CharField(max_length = 50)
    charge = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.area_type} - {self.location} : {self.charge}'
    

    
    
