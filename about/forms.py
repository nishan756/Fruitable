from .models import Contact
from django import forms 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ["created_at"]
        widgets = {
            "name":forms.TextInput(
                attrs = {
                    "type":'text',
                    "class":"form-control",
                    "placeholder":'Your Name',
                }
            ),
            "email":forms.EmailInput(
                attrs = {
                    "type":'email',
                    "class":"form-control",
                    "placeholder":'Enter Email',
                }
            ),
            "subject":forms.TextInput(
                attrs = {
                    "type":'text',
                    "class":"form-control",
                    "placeholder":'Message Subject',
                }
            ),
        }