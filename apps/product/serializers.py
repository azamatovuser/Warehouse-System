from rest_framework import serializers
from apps.product.models import Spare, Device


class DeviceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'client', 'name', 'imei')


class DeviceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'client', 'name', 'imei']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        client = instance.client
        representation['client'] = client.full_name if client and client.full_name else client.username if client and client.username else client.id if client else None

        return representation


class SpareCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spare
        fields = '__all__'