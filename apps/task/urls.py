from django.urls import path
from apps.task.views import TaskListAPIView, TaskCreateAPIView


urlpatterns = [
    path('list/', TaskListAPIView.as_view()),
    path('create/', TaskCreateAPIView.as_view()),
]