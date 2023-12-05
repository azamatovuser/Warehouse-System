from django.db import models
from apps.account.models import Account
from apps.storage.models import Storage
from apps.product.models import Device
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta


class Order(models.Model):
    client = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='client_order')
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True, related_name='device_order')
    storage = models.ManyToManyField(Storage, null=True, blank=True, related_name='storage_order')
    problem_description = models.TextField(null=True)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    deadline = models.DateField(null=True)
    is_done = models.BooleanField(default=False, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    is_notificated = models.BooleanField(default=False, null=True)


class Notification(models.Model):
    employee = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    message = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Notification)
def delete_old_notifications(sender, instance, **kwargs):
    cutoff_date = timezone.now()
    Notification.objects.filter(created_date__lt=cutoff_date).delete()