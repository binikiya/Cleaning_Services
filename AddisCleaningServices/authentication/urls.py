from django.urls import path
from .views import LoginPageView, UserPageView, AdminPageView


app_name = 'authentication'

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('user/', UserPageView.as_view(), name='user'),
    path('admin/', AdminPageView.as_view(), name='admin'),
]
