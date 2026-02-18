from django.urls import path, include
from .api_views import CartItemDetailView, CartItemView


urlpatterns = [

    path('carts/', CartItemView),
    path('carts/<int:pk>/', CartItemDetailView)
]