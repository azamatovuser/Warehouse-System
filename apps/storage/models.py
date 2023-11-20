from django.db import models
from apps.product.models import Spare


class Storage(models.Model):
    spare = models.ForeignKey(Spare, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)