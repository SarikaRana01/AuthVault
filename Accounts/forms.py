# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import SignUpModel


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    pin = forms.CharField(
        widget=forms.PasswordInput,
        min_length=6,
        max_length=8,
    )

