from django.urls import path
from .views import SubscriptionListCreateView  

urlpatterns = [
    path('subscriptions/', SubscriptionListCreateView.as_view(), name='subscription-list-create'),
]
