from .models import ProductReview
from django import forms 

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ["point" , "review"]

