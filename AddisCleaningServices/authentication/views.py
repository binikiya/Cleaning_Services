from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Login
from pricing.models import Payment


class LoginPageView(TemplateView):
    template_name = 'authentication/login.html'

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        e = Login.objects.get().email
        p = Login.objects.get().password

        if e == email and p == password:
            response = redirect('auth:admin')
            return response
        else:
            messages.error(request, "Please enter correct identification")

        return render(request, 'authentication/login.html')

class UserPageView(TemplateView):
    template_name = 'base.html'


class AdminPageView(TemplateView):
    template_name = "admin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["payment"] = Payment.objects.all()
        i = 1
        return context