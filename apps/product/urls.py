from django.urls import path
from apps.product.views import (SpareListAPIView,
                                DeviceListCreateAPIView,
                                DeviceDeleteAPIView,
                                DeviceDetailAPIView,
                                SpareCreateAPIView,
                                SpareDetailAPIView,
                                SpareDeleteAPIView)

urlpatterns = [
    path('spare_list/', SpareListAPIView.as_view()),
    path('spare_create/', SpareCreateAPIView.as_view()),
    path('spare_detail/<int:pk>', SpareDetailAPIView.as_view()),
    path('spare_delete/<int:pk>', SpareDeleteAPIView.as_view()),
    path('device_list_or_create/', DeviceListCreateAPIView.as_view()),
    path('device/detail/<int:pk>/', DeviceDetailAPIView.as_view()),
    path('device/delete/<int:pk>/', DeviceDeleteAPIView.as_view()),
]