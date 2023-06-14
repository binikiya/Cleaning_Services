from django.urls import path
from .views import PricingPageView, NameValidationView, NickValidation, \
EmailValidation, DobValidation, NumberValidation, CvcValidation, ExpiryValidation
from django.views.decorators.csrf import csrf_exempt


app_name = 'pricing'

urlpatterns = [
    path('register/', PricingPageView.as_view(), name='register'),

    path('name-validation', csrf_exempt(NameValidationView.as_view()), name='name-validation'),
    path('nick-validation', csrf_exempt(NickValidation.as_view()), name='nick-validation'),
    path('email-validation', csrf_exempt(EmailValidation.as_view()), name='email-validation'),
    path('dob-validation', csrf_exempt(DobValidation.as_view()), name='dob-validation'),
    path('number-validation', csrf_exempt(NumberValidation.as_view()), name='number-validation'),
    path('cvc-validation', csrf_exempt(CvcValidation.as_view()), name='cvc-validation'),
    path('expiry-validation', csrf_exempt(ExpiryValidation.as_view()), name='expiry-validation'),
]
