
def About(request):
    from .models import AboutShop
    about = AboutShop.objects.first()
    phones = None
    if about:
        phones = about.phone.split(',')
    return {"about":about , "phones":phones}
