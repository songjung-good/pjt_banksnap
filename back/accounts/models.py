from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from bank.models import Bank


class User(AbstractUser):
    pass


class Propensity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    deposit_now = models.IntegerField(default=0)
    deposit_type = models.CharField(max_length=10, default='미선택')
    income = models.IntegerField(default=0)
    age = models.IntegerField(default=0)