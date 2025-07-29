# accounts/models.py

from django.db import models
from django.contrib.auth.models import User

class SignUpModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    pin = models.CharField(max_length=8)

    def _str_(self):
        return self.user.username

