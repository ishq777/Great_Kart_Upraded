from django.urls import path, include
from orders.api_views import PaymentView,OrderView

urlpatterns = [

    path('orders/', OrderView.as_view()),
    path('payments/', PaymentView.as_view()),
]