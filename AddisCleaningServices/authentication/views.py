from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Login


class LoginPageView(TemplateView):
    template_name = 'authentication/login.html'

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        e = Login.objects.get().email
        p = Login.objects.get().password

        if e == email and p == password:
            return render(request, 'admin.html')
        else:
            messages.error(request, "Please enter correct identification")

        return render(request, 'authentication/login.html')

class UserPageView(TemplateView):
    template_name = 'base.html'


class AdminPageView(TemplateView):
    template_name = 'admin.html'