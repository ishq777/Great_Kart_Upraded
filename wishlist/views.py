from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from store.models import Product, Variation
from django.contrib.auth.decorators import login_required
from accounts.views import login
from django.contrib import messages
from carts.models import CartItem


# def wishlist_id(request):
#     wishlist = request.session.session_key #ask browser for existing key
#     if not wishlist:
#         wishlist = request.session.create() #if there isn't one, create one
#     return wishlist


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    product_variations = []

    # similar to add cart views
    if request.method == "POST":
        for key, value in request.POST.items():
            try:
                variation = Variation.objects.get(
                    product=product,
                    variation_category__iexact=key,
                    variation_value__iexact=value,
                    is_active=True,
                )
                product_variations.append(variation)
            except Variation.DoesNotExist:
                continue

    # Require variation selection when product has active variations
    if product.variation_set.filter(is_active=True).exists() and not product_variations:
        messages.error(request, "Select variation.")
        return redirect(product.get_url())

    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    if product_variations:
        wishlist_item.variations.set(product_variations)

    return redirect('wishlist')




@login_required
def move_to_cart(request, product_id):
    wishlist_item = get_object_or_404(
        Wishlist,
        user=request.user,
        product_id=product_id,
    )

    product = wishlist_item.product
    product_variations = list(wishlist_item.variations.all())

    cart_items = CartItem.objects.filter(
        products=product,
        user=request.user,
    )

    target_variation_ids = sorted([v.id for v in product_variations])
    matched_item = None
    for item in cart_items:
        item_variation_ids = sorted(list(item.variations.values_list("id", flat=True)))
        if item_variation_ids == target_variation_ids:
            matched_item = item
            break

    if matched_item:
        matched_item.quantity += 1
        matched_item.save()
    else:
        cart_item = CartItem.objects.create(
            products=product,
            quantity=1,
            user=request.user,
            cart=None,
        )
        if product_variations:
            cart_item.variations.add(*product_variations)

    wishlist_item.delete()
    return redirect('cart')




    

@login_required(login_url=login)
def wishlist(request):

    items = Wishlist.objects.filter(user=request.user)

    context = {
        'wishlist_items' : items
    }

    return render(request, 'store/wishlist.html', context)


@login_required(login_url=login)
def remove_from_wishlist(request,product_id):

    Wishlist.objects.filter(user=request.user ,product_id = product_id).delete()

    return redirect('wishlist')
