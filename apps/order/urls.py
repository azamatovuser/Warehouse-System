from django.urls import path
from apps.order.views import OrderCreateAPIView, OrderListAPIView, OrderRUDAPIView


urlpatterns = [
    path('create/', OrderCreateAPIView.as_view()),
    path('list/', OrderListAPIView.as_view()),
    path('detail/<int:pk>/', OrderRUDAPIView.as_view()),
]