
from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('support/', include('support.urls')),

    #api routing
    path('api/v1/', include('store.api_urls')),
    path('api/v1/', include('orders.api_urls')),
    path('api/v1/', include('category.api_urls')),
    path('api/v1/', include('carts.api_urls')),
    path('api/v1/', include('accounts.api_urls')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
