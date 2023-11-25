from django.urls import path
from apps.task.views import TaskListAPIView, TaskCreateAPIView, TaskRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('list/', TaskListAPIView.as_view()),
    path('create/', TaskCreateAPIView.as_view()),
    path('list/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view()),
]