from django.urls import path
from apps.storage.views import MonthlyOrderListAPIView, DailyOrderListAPIView, StorageListAPIView


urlpatterns = [
    path('list/', StorageListAPIView.as_view()),
    path('analytics/monthly_order/', MonthlyOrderListAPIView.as_view()),
    path('analytics/daily_order/', DailyOrderListAPIView.as_view()),
]
