from django.db import models
from django.utils import timezone


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=140, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=13, blank=False, null=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    name1 = models.CharField(max_length=120, blank=False, null=False)
    message = models.TextField(blank=False)
    email1 = models.EmailField(max_length=100, blank=False, null=False)
    phone1 = models.CharField(max_length=13, blank=False, null=False)
    date1 = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name1