from django.urls import path
from .views import PricingPageView


app_name = 'pricing'

urlpatterns = [
    path('register/', PricingPageView.as_view(), name='register'),
]
