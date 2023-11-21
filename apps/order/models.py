from django.db import models
from apps.account.models import Account
from apps.storage.models import Storage
from apps.product.models import Device


class Order(models.Model):
    client = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='client_order')
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True, related_name='device_order')
    storage = models.ManyToManyField(Storage, null=True, blank=True, related_name='storage_order')
    problem_description = models.TextField(null=True)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    is_done = models.BooleanField(default=False, null=True)
    created_date = models.DateTimeField(auto_now_add=True)