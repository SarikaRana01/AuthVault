from django import forms
from .models import Vault

class VaultForm(forms.ModelForm):
    class Meta:
        model = Vault
        exclude=['user']
        fields = ['platform', 'username', 'encrypted_password', 'notes']
        widgets = {
            'platform': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username',
                'required': True
            }),
            'encrypted_password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter password',
                'required': True
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter any notes...',
                'rows': 2
            }),
        }