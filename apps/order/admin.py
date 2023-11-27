from django.contrib import admin
from apps.order.models import Order, Notification


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'device', 'price', 'deadline')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'order')