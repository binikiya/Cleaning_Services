from django.shortcuts import render
from django.views.generic import TemplateView


class LoginPageView(TemplateView):
    template_name = 'authentication/login.html'


class UserPageView(TemplateView):
    template_name = 'base.html'