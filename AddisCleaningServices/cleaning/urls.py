from django.urls import path
from .views import HomePageView, UsernameValidationView, AddressValidationView, \
    EmailValidationView, PhoneValidationView, NameValidationView, \
    MessageValidationView, EmailValidationView1, PhoneValidationView1
from django.views.decorators.csrf import csrf_exempt

app_name = 'cleaning'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name='validate-username'),
    path('validate-address', csrf_exempt(AddressValidationView.as_view()), name='validate-address'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validate-email'),
    path('validate-phone', csrf_exempt(PhoneValidationView.as_view()), name='validate-phone'),

    path('validate-name-one', csrf_exempt(NameValidationView.as_view()), name='validate-name-one'),
    path('validate-message-one', csrf_exempt(MessageValidationView.as_view()), name='validate-message-one'),
    path('validate-email-one', csrf_exempt(EmailValidationView1.as_view()), name='validate-email-one'),
    path('validate-phone-one', csrf_exempt(PhoneValidationView1.as_view()), name='validate-phone-one'),
]
