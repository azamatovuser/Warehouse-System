from django.urls import path
from apps.order.views import OrderCreateAPIView


urlpatterns = [
    path('create/', OrderCreateAPIView.as_view()),
]