from rest_framework import serializers

from orders.models import Order, OrderProduct, Payment


class OrderSerializer(serializers.ModelSerializer):

    user = serializers.CharField(source='user.username', read_only=True)
    payment_id = serializers.CharField(source='payment.payment_id', read_only=True)
    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'full_name',
            'payment_id',
            'order_number',
            'order_total',
            'status',
        ]


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Payment
        fields = "__all__"