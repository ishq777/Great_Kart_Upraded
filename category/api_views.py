from rest_framework import viewsets
from .models import Category
from rest_framework.filters import SearchFilter
from orders.api_views import MyPagination
from .serializers import CategorySerializer



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter]
    search_fields = ['category_name' ]


