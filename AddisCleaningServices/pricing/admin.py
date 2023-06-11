from django.contrib import admin
from .models import Payment


class AdminPayment(admin.ModelAdmin):
    pass
admin.site.register(Payment, AdminPayment)