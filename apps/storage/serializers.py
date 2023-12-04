from rest_framework import serializers
from apps.storage.models import Storage


class StorageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        spare = instance.spare
        representation['spare'] = spare.name if spare and spare.name else spare.id

        return representation


class OrderTotalSerializer(serializers.Serializer):
    total_price = serializers.DecimalField(max_digits=25, decimal_places=2)