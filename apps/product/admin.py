from django.contrib import admin
from apps.product.models import Spare, Device


@admin.register(Spare)
class SpareAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_price', 'last_price')
    search_fields = ('name', )


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'imei')
    search_fields = ('client', 'name', 'imei')