from rest_framework.routers import DefaultRouter
from  store.api_views import ProductView
# VariationView, ProductDetailView, VariationDetailView
from django.urls import path, include


router = DefaultRouter()
router.register('products', ProductView, basename='products')


urlpatterns = [


    # path('products/', ProductView),
    # path('products/<int:pk>/', ProductDetailView),

    # path('variations/', VariationView),
    # path('variations/<int:pk>/', VariationDetailView),

    path ('' , include(router.urls)),
]


