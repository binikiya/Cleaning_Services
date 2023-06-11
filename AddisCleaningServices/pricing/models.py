from django.db import models
from django.utils import timezone


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    cleaning_id = models.BigIntegerField()
    name = models.CharField(max_length=200, default=False, null=False)
    nick = models.CharField(max_length=80, default=False)
    email = models.EmailField(max_length=120, default=False, null=False)
    dob = models.DateField()
    gender = models.CharField(max_length=10, default=False, null=False)
    card = models.CharField(max_length=30, default=False, null=False)
    number = models.CharField(max_length=40, default=False, null=False)
    cvc = models.CharField(max_length=6, default=False, null=False)
    expiry = models.DateField()
    current = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name