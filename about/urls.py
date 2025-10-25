from .views import Conditions , Contact
from django.urls import path

urlpatterns = [
    path("conditions/",Conditions,name = "conditions"),
    path("contact/",Contact,name = "contact"),
    
]
