from django.urls import path
from apps.product.views import SpareListAPIView


urlpatterns = [
    path('spare_list/', SpareListAPIView.as_view()),
]