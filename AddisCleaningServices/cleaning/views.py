from typing import Any
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import Post


class HomePageView(TemplateView):
    template_name = 'index.html'

    def post(self, request):
        name = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']

        user = Post.objects.create(
            name = name,
            address = address,
            email = email,
            phone = phone
        )
        user.save()

        return render(request, 'index.html')
