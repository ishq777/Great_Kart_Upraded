from rest_framework import generics
from orders.serializers import OrderProductSerializer,OrderSerializer,PaymentSerializer
from orders.models import Payment, Order, OrderProduct
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    page_size = 3


class OrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, OrderingFilter]
    
    search_fields = ['user','order_number', 'first_name', 'phone','email' ]
    ordering_fields = ['order_number','created_at']


class PaymentView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user', 'payment_id' ]
    ordering_fields = ['id', 'payment_id']