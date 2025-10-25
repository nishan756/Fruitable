from .models import ConfirmOrder
from django import forms 

class OrderForm(forms.ModelForm):
    class Meta:
        model = ConfirmOrder
        exclude = ["cart","date","items","price","status"]
        widgets = {
            "name":forms.TextInput(
                attrs = {
                    "type":'text',
                    "placeholder":"Your Name",
                    "class":'form-control'
                }
            ),
            "email":forms.EmailInput(
                attrs = {
                    "type":'email',
                    "placeholder":"Your Email",
                    "class":'form-control'
                }
            ),
            "phone":forms.TextInput(
                attrs = {
                    "type":'tel',
                    "placeholder":"Your Phone",
                    "class":'form-control'
                }
            ),
            "location":forms.TextInput(
                attrs = {
                    "type":'text',
                    "placeholder":"Your Location",
                    "class":'form-control'
                }
            ),
            "shipping_charge":forms.Select(
                attrs = {
                    "type":'select',
                    "placeholder":"Your Location",
                    "class":'form-control'
                }
            )
        }