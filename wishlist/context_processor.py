from .models import Wishlist
from .import views
from store.models import Product


def counter(request):

    wishlist_count = 0

    if 'admin' in request.path:
        return {}
    
    if request.user.is_authenticated:
        wishlist_count = Wishlist.objects.filter(user=request.user).count()

    
    return dict(wishlist_count=wishlist_count)


        

