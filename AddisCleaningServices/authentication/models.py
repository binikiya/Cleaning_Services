from django.db import models


class Login(models.Model):
    email = models.EmailField(max_length=100, default=False, null=False)
    username = models.CharField(max_length=140, default=False, null=False)
    password = models.CharField(max_length=100, default=False, null=False)