from django.utils.deprecation import MiddlewareMixin
from .models import Cart
from django.db.models import Q

class SessionKeyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        cart = None
        if request.user.is_authenticated:
            cart , created = Cart.objects.get_or_create(user = request.user)
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
            cart , created = Cart.objects.get_or_create(session_key = session_key)
        
        request.cart = cart
