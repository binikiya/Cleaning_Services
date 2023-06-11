from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Payment
from django.contrib import messages


class PricingPageView(TemplateView):
    template_name = 'pricing/register.html'
    
    def post(self, request):
        id = 1
        name = request.POST['name']
        name2 = request.POST['name2']
        email = request.POST['email']

        date = request.POST['date']
        month = request.POST['month']
        year = request.POST['year']
        dob = year + '-' + month + '-' + date

        gender = request.POST['gender']
        card = request.POST['pay']
        number = request.POST['card']
        cvc = request.POST['cvc']

        datee = request.POST['datee']
        monthe = request.POST['monthe']
        yeare = request.POST['yeare']
        expiry = yeare + '-' + monthe + '-' + datee

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
            expiry = expiry
        )

        pay.save()
        messages.success(request, "Your Payment is successfull please see your email for your confirmed payment.")
        
        return render(request, 'pricing/register.html')