from django.contrib import admin
from .models import Login


class AdminLogin(admin.ModelAdmin):
    pass

admin.site.register(Login, AdminLogin)