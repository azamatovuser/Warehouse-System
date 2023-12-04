from rest_framework import serializers
from apps.storage.models import Storage


class StorageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'


class OrderTotalSerializer(serializers.Serializer):
    total_price = serializers.DecimalField(max_digits=25, decimal_places=2)