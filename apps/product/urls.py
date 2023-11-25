from django.urls import path
from apps.product.views import SpareListAPIView, DeviceListCreateAPIView

urlpatterns = [
    path('spare_list/', SpareListAPIView.as_view()),
    path('device/', DeviceListCreateAPIView.as_view()),
]