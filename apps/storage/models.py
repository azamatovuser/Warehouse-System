from django.db import models
from apps.product.models import Spare


class Storage(models.Model):
    spare = models.ForeignKey(Spare, on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)