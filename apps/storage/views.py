from rest_framework import generics
from apps.storage.serializers import StorageListSerializer
from apps.order.models import Order
from apps.storage.models import Storage
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from calendar import monthrange


class StorageListAPIView(generics.ListCreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageListSerializer


class MonthlyOrderListAPIView(APIView):
    def get(self, request):
        # Get the current date
        current_date = timezone.now()

        # Calculate the first day of the current month
        current_month_start = current_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        # Calculate the last day of the current month
        _, last_day_of_month = monthrange(current_date.year, current_date.month)
        current_month_end = current_date.replace(day=last_day_of_month, hour=23, minute=59, second=59, microsecond=999999)

        # Filter orders created between the first and last day of the current month
        orders_count = Order.objects.filter(
            created_date__range=(current_month_start, current_month_end)
        ).count()

        response_data = {
            "message": f"{orders_count} заказов в этом месяце"
        }

        return Response(response_data)


class DailyOrderListAPIView(APIView):
    def get(self, request):
        # Get the current date
        current_date = timezone.now()

        # Calculate the start of the current day
        current_day_start = current_date.replace(hour=0, minute=0, second=0, microsecond=0)

        # Calculate the end of the current day
        current_day_end = current_date.replace(hour=23, minute=59, second=59, microsecond=999999)

        # Filter orders created between the start and end of the current day
        orders_count = Order.objects.filter(
            created_date__range=(current_day_start, current_day_end)
        ).count()

        response_data = {
            "message": f"{orders_count} заказов сегодня"
        }

        return Response(response_data)
