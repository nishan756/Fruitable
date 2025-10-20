from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

class CustomBackend(ModelBackend):

    def authenticate(self, request, username = None , password = None):
        User = get_user_model()
        try:
            user = User.objects.get(Q(username = username)|Q(phone = username)|Q(email = username))
        except User.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        return None