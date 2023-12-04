from rest_framework import generics
from apps.storage.serializers import StorageListSerializer, OrderTotalSerializer
from apps.order.models import Order
from apps.account.models import Account
from apps.storage.models import Storage
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from calendar import monthrange
from django.db.models import Sum


class StorageListAPIView(generics.ListCreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageListSerializer


class StorageAvailableListAPIView(generics.ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageListSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_booked=False)


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


class OrderTotalPriceAPIView(APIView):
    def get(self, request):
        # Calculate the sum of all prices
        total_price = Order.objects.aggregate(total_price=Sum('price'))['total_price'] or 0

        # Serialize the result using the correct serializer
        serializer = OrderTotalSerializer({"total_price": total_price})

        return Response(serializer.data)


class ClientMonthlyAPIView(APIView):
    def get(self, request):
        # Get the current date
        current_date = timezone.now()

        # Calculate the first day of the current month
        current_month_start = current_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        # Calculate the last day of the current month
        _, last_day_of_month = monthrange(current_date.year, current_date.month)
        current_month_end = current_date.replace(day=last_day_of_month, hour=23, minute=59, second=59, microsecond=999999)

        # Filter clients created between the first and last day of the current month
        clients_count = Account.objects.filter(
            date_created__range=(current_month_start, current_month_end),
            role=2  # Assuming 'Client' role is 2
        ).count()

        response_data = {
            "message": f"{clients_count} клиенты присоединились за {current_month_start.strftime('%B %Y')}."
        }

        return Response(response_data)


class ClientWeeklyAPIView(APIView):
    def get(self, request):
        # Get the current date
        current_date = timezone.now()

        # Calculate the start of the current week (Monday)
        current_week_start = current_date - timezone.timedelta(days=current_date.weekday())
        current_week_start = current_week_start.replace(hour=0, minute=0, second=0, microsecond=0)

        # Calculate the end of the current week (Sunday)
        current_week_end = current_week_start + timezone.timedelta(days=6)
        current_week_end = current_week_end.replace(hour=23, minute=59, second=59, microsecond=999999)

        # Filter clients created between the start and end of the current week
        clients_count = Account.objects.filter(
            date_created__range=(current_week_start, current_week_end),
            role=2  # Assuming 'Client' role is 2
        ).count()

        response_data = {
            "message": f"{clients_count} клиентов добавились на этой недели"
        }

        return Response(response_data)


class ClientYearlyAPIView(APIView):
    def get(self, request):
        # Get the current date
        current_date = timezone.now()

        # Calculate the first day of the current year
        current_year_start = current_date.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)

        # Calculate the last day of the current year
        current_year_end = current_date.replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999999)

        # Filter clients created between the first and last day of the current year
        clients_count = Account.objects.filter(
            date_created__range=(current_year_start, current_year_end),
            role=2  # Assuming 'Client' role is 2
        ).count()

        response_data = {
            "message": f"{clients_count} клиенты добавились за этот год"
        }

        return Response(response_data)


class ClientDailyAPIView(APIView):
    def get(self, request):
        # Get the current date
        current_date = timezone.now()

        # Calculate the start of the current day
        current_day_start = current_date.replace(hour=0, minute=0, second=0, microsecond=0)

        # Calculate the end of the current day
        current_day_end = current_date.replace(hour=23, minute=59, second=59, microsecond=999999)

        # Filter clients created between the start and end of the current day
        clients_count = Account.objects.filter(
            date_created__range=(current_day_start, current_day_end),
            role=2  # Assuming 'Client' role is 2
        ).count()

        response_data = {
            "message": f"{clients_count} клиенты за сегодня"
        }

        return Response(response_data)
