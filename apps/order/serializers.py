from rest_framework import serializers
from apps.order.models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('client', 'device', 'storage', 'problem_description', 'price')