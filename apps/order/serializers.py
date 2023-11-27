from rest_framework import serializers
from apps.order.models import Order, Notification


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'client', 'device', 'storage', 'problem_description', 'price', 'deadline', 'is_done')


class OrderListSerializer(serializers.ModelSerializer):
    client_full_name = serializers.SerializerMethodField()
    device_name = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ('id', 'client_full_name', 'device_name', 'price', 'deadline')

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
        fields = ('id', 'client_full_name', 'device_name', 'storages', 'problem_description', 'price', 'deadline', 'is_done')

    def get_client_full_name(self, obj):
        return obj.client.full_name if obj.client else None

    def get_device_name(self, obj):
        return obj.device.name if obj.device else None

    def get_storages(self, obj):
        return [storage.spare.name for storage in obj.storage.all()] if obj.storage.exists() else []


class OrderUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'