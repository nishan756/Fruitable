from .models import ProductReview , ProductRequest
from django import forms 

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ["point" , "review"]

class RequestForm(forms.ModelForm):
    class Meta:
        model = ProductRequest
        exclude = ["user","date","product"]
        widgets = {
            'name':forms.TextInput(
                attrs = {
                    'type':'text',
                    "class":"form-control",
                    "placeholder":"Enter Name"
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'type':'text',
                    "class":"form-control",
                    "placeholder":"Enter Email"
                }
            ),
            'message':forms.Textarea(
                attrs = {
                    'type':'text',
                    "class":"form-control",
                    "placeholder":"Your Message"
                }
            )
        }
