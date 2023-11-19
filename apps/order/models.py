from django.db import models
from apps.account.models import Account
from apps.product.models import Device


class Order(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)
    problem_description = models.TextField()
    price = models.DecimalField(max_digits=25, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device