from django.db import models
from apps.account.models import Account
from apps.product.models import Device


class Order(models.Model):
    client = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='client_order')
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True, related_name='device_order')
    problem_description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)