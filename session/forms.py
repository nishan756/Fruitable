from .models import CustomUser
from django import forms 

class CustomUserForm(forms.ModelForm):
    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.order_fields(["first_name","last_name","username","email","phone"])
    class Meta:
        model = CustomUser
        exclude = ["date_joined","last_login","is_superuser","is_staff","is_active","groups","user_permissions"]
        widgets = {
            "first_name":forms.TextInput(attrs = {"type":'text','placeholder':'First Name'}),
            "last_name":forms.TextInput(attrs = {"type":'text','placeholder':'Last Name'}),
            "username":forms.TextInput(attrs = {"type":'text','placeholder':'Username'}),
            "email":forms.TextInput(attrs = {"type":'email','placeholder':'Email'}),
            "password":forms.TextInput(attrs = {"type":'text','placeholder':'Password'}),
            "phone":forms.TextInput(attrs = {"type":'text','placeholder':'Phone'}),

        }
