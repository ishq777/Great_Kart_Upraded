from django.urls import path
from .api_views import AccountView, AccountDetailView


urlpatterns = [

    path('account/' , AccountView),
    path('account/<int:pk>/' , AccountDetailView),

]