from django import forms
from django.utils import timezone


class PostForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()