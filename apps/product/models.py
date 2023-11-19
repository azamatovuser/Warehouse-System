from django.db import models
from apps.account.models import Account


class Spare(models.Model):
    name = models.CharField(max_length=221)
    first_price = models.DecimalField(max_digits=25, decimal_places=2)
    last_price = models.DecimalField(max_digits=25, decimal_places=2)
    bought_date = models.DateTimeField(null=True, blank=True)
    sold_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=221)
    imei = models.CharField(max_length=221)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
