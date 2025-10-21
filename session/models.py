from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length = 150 , blank = True , null = True , unique = True)
    image = CloudinaryField("image" , folder = "fruitable/user_image" , blank = True , null = True)
    email = models.EmailField(unique = True , blank = True , null = True)
    phone = models.CharField(max_length = 11 , blank = True , null = True , unique = True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["first_name","last_name","phone",]

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'