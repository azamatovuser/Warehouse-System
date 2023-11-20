from django.db import models
from apps.account.models import Account
from apps.product.models import Device


class Task(models.Model):
    title = models.CharField(max_length=221)
    manager = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='manager_task')
    employee = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='employee_task')
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True, related_name='device_task')
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title