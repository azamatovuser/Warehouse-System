from rest_framework import generics
from apps.order.models import Order
from apps.storage.models import Storage
from apps.order.serializers import OrderCreateSerializer
from rest_framework import serializers


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer):
        storage_data_list = serializer.validated_data.get('storage')

        is_any_storage_booked = False

        for storage_data in storage_data_list:
            try:
                storage = Storage.objects.get(id=storage_data.id)
            except Storage.DoesNotExist:
                raise serializers.ValidationError("Storage with id {} does not exist".format(storage_data.id))

            if storage.is_booked:
                is_any_storage_booked = True
                break

        if is_any_storage_booked:
            raise serializers.ValidationError("At least one storage is already booked.")


        for storage_data in storage_data_list:
            storage = Storage.objects.get(id=storage_data.id)
            storage.is_booked = True
            storage.save()

        order = serializer.save()
        return order