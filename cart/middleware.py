from django.utils.deprecation import MiddlewareMixin
from .models import Cart
from django.db.models import Q
from session.models import CustomUser

class SessionKeyMiddleware(MiddlewareMixin):
    def process_request(self , request):
        if request.user.is_authenticated:
            cart , created = Cart.objects.get_or_create(user__id = request.user.id)
        else:
            session_key = request.session.get("session_key")
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
            cart = Cart.objects.create(session_key = session_key)
        request.cart = cart
    