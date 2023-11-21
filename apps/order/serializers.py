from rest_framework import serializers
from apps.order.models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('client', 'device', 'storage', 'problem_description', 'price')


class OrderListSerializer(serializers.ModelSerializer):
    client_full_name = serializers.SerializerMethodField()
    device_name = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ('client_full_name', 'device_name', 'price')

    def get_client_full_name(self, obj):
        return obj.client.full_name if obj.client else None

    def get_device_name(self, obj):
        return obj.device.name if obj.device else None


class OrderDetailSerializer(serializers.ModelSerializer):
    client_full_name = serializers.SerializerMethodField()
    device_name = serializers.SerializerMethodField()
    storages = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ('client_full_name', 'device_name', 'storages', 'problem_description', 'price', 'is_done')

    def get_client_full_name(self, obj):
        return obj.client.full_name if obj.client else None

    def get_device_name(self, obj):
        return obj.device.name if obj.device else None

    def get_storages(self, obj):
        return [storage.spare.name for storage in obj.storage.all()] if obj.storage.exists() else []