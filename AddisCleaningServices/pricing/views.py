from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Payment
from django.contrib import messages
from django.views import View
import json
from django.http import JsonResponse
from validate_email import validate_email


class PricingPageView(TemplateView):
    template_name = 'pricing/register.html'
    
    def post(self, request):
        id = 1
        name = request.POST['name']
        name2 = request.POST['nick']
        email = request.POST['email']

        date = request.POST['date']
        month = request.POST['month']
        year = request.POST['year']
        dob = year + '-' + month + '-' + date

        gender = request.POST['gender']
        price = request.POST['price']
        card = request.POST['pay']
        number = request.POST['card']
        cvc = request.POST['cvc']

        datee = request.POST['datee']
        monthe = request.POST['monthe']
        yeare = request.POST['yeare']
        expiry = yeare + '-' + monthe + '-' + datee

        pay = 0

        if price == "Basic":
            pay = 15000
        if price == "Standard":
            pay = 20000
        if price == "Premium":
            pay = 25000

        pay = Payment.objects.create(
            cleaning_id = id,
            name = name,
            nick = name2,
            email = email,
            dob = dob,
            gender = gender,
            card = card,
            number = number,
            cvc = cvc,
            expiry = expiry,
            price = pay
        )

        pay.save()
        messages.success(request, "Your Payment is successfull please contact us if you don't get a confirmation email in 2 hours.")
        
        return render(request, 'pricing/register.html')
    

class NameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data['name']
        if str(name) == "":
            return JsonResponse({'username_error': 'Name should contain alphanumeric characters'}, status = 400)
        return JsonResponse({'username_valid': True})
    

class NickValidation(View):
    pass


class EmailValidation(View):
    pass


class DobValidation(View):
    pass


class NumberValidation(View):
    pass


class CvcValidation(View):
    pass


class ExpiryValidation(View):
    pass