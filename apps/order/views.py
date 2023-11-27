from rest_framework import generics
from apps.order.models import Order, Notification
from apps.storage.models import Storage
from apps.order.serializers import OrderCreateSerializer, \
    OrderListSerializer, OrderDetailSerializer, \
    OrderUpdateDeleteSerializer, NotificationSerializer
from rest_framework import serializers
from rest_framework.views import APIView
from datetime import date, timedelta
from rest_framework.response import Response
from rest_framework import status


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


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer


class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateDeleteSerializer

    def perform_update(self, serializer):
        instance = serializer.instance
        storage_data_list = serializer.validated_data.get('storage')

        for existing_storage in instance.storage.all():
            if existing_storage not in [storage_data.spare for storage_data in storage_data_list]:
                existing_storage.is_booked = False
                existing_storage.save()

        for storage in storage_data_list:
            storage.is_booked = True
            storage.save()

        instance = serializer.save()



class OrderDeleteAPIView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateDeleteSerializer

    def perform_destroy(self, instance):
        for storage_data in instance.storage.all():
            storage_data.is_booked = False
            storage_data.save()

        instance.delete()


class NotificationListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        today = date.today()

        for order in orders:
            deadline_date = order.deadline
            time_difference = deadline_date - today
            if time_difference <= timedelta(days=1) and not order.is_notificated:
                Notification.objects.create(
                    employee=order.client,
                    order=order,
                    message=f"Ваш заказ - {order.device.name} должен быть закончен в течение дня, поспешите пожалуйста"
                )

                order.is_notificated = True
                order.save()

        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)