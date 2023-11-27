from django.urls import path
from apps.order.views import OrderCreateAPIView, OrderListAPIView, \
    OrderDetailAPIView, OrderUpdateAPIView, OrderDeleteAPIView, \
    NotificationListAPIView



urlpatterns = [
    # order
    path('create/', OrderCreateAPIView.as_view()),
    path('list/', OrderListAPIView.as_view()),
    path('detail/<int:pk>/', OrderDetailAPIView.as_view()),
    path('update/<int:pk>/', OrderUpdateAPIView.as_view()),
    path('delete/<int:pk>/', OrderDeleteAPIView.as_view()),

    # notification
    path('notification_list/', NotificationListAPIView.as_view()),
]