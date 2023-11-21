from rest_framework import generics
from apps.task.models import Task
from apps.task.serializers import TaskListSerializer, TaskCreateSerializer


class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer