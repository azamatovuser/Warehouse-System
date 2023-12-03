from rest_framework import serializers
from apps.storage.models import Storage


class StorageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'