from rest_framework import serializers
from apps.product.models import Spare, Device


class DeviceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('client', 'name', 'imei')


class DeviceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class SpareCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spare
        fields = '__all__'