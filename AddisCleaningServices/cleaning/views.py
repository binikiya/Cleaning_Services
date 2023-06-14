from typing import Any
from django.views.generic import TemplateView
from .models import Post
from django.shortcuts import redirect, render
from django.views import View
import json
from django.http import JsonResponse
from validate_email import validate_email


class HomePageView(TemplateView):
    template_name = 'index.html'

    def post(self, request):
        name = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']

        # price = request.POST['price']

        user = Post.objects.create(
            name = name,
            address = address,
            email = email,
            phone = phone
        )
        user.save()
        
        response = redirect('pricing:register')
        return response


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data['name']
        if not str(name).isalnum():
            return JsonResponse({'username_error': 'Name should contain alphanumeric characters'}, status = 400)
        return JsonResponse({'username_valid': True})


class AddressValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        address = data['address']
        if str(address) == "":
            return JsonResponse({'address_error': 'Address should not be empty'}, status = 400)
        return JsonResponse({'address_valid': True})


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email should be on its format'}, status = 400)
        return JsonResponse({'email_valid': True})


class PhoneValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        phone = data['phone']

        if not str(phone).isnumeric():
            return JsonResponse({'phone_error': 'Phone should contain numeric characters'}, status = 400)
        return JsonResponse({'phone_valid': True})
    

# comment section
class NameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        name1 = data['name1']
        if not str(name1).isalnum():
            return JsonResponse({'username_error': 'Name should contain alphanumeric characters'}, status = 400)
        return JsonResponse({'username_valid': True})


class MessageValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        message = data['message']
        if str(message) == "":
            return JsonResponse({'address_error': 'Message should not be empty'}, status = 400)
        return JsonResponse({'address_valid': True})


class EmailValidationView1(View):
    def post(self, request):
        data = json.loads(request.body)
        email1 = data['email1']
        if not validate_email(email1):
            return JsonResponse({'email_error': 'Email should be on its format'}, status = 400)
        return JsonResponse({'email_valid': True})


class PhoneValidationView1(View):
    def post(self, request):
        data = json.loads(request.body)
        phone1 = data['phone1']

        if not str(phone1).isnumeric():
            return JsonResponse({'phone_error': 'Phone should contain numeric characters'}, status = 400)
        return JsonResponse({'phone_valid': True})