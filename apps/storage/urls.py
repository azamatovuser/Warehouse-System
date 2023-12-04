from django.urls import path
from apps.storage.views import MonthlyOrderListAPIView, DailyOrderListAPIView, StorageListAPIView, \
    OrderTotalPriceAPIView, ClientMonthlyAPIView, ClientWeeklyAPIView, ClientYearlyAPIView, ClientDailyAPIView, StorageAvailableListAPIView

urlpatterns = [
    path('list_or_create/', StorageListAPIView.as_view()),
    path('available_list/', StorageAvailableListAPIView.as_view()),
    path('analytics/monthly_order/', MonthlyOrderListAPIView.as_view()),
    path('analytics/daily_order/', DailyOrderListAPIView.as_view()),
    path('analytics/order_total_price/', OrderTotalPriceAPIView.as_view()),
    path('analytics/yearly_client/', ClientYearlyAPIView.as_view()),
    path('analytics/monthly_client/', ClientMonthlyAPIView.as_view()),
    path('analytics/weekly_client/', ClientWeeklyAPIView.as_view()),
    path('analytics/daily_client/', ClientDailyAPIView.as_view()),
]
