from django.urls import path, include
from .api_views import CategoryViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')

urlpatterns = [

    path('', include(router.urls))
]



