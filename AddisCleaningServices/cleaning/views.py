from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
from django.shortcuts import redirect


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
        response = redirect('authentication:user')

        return response
