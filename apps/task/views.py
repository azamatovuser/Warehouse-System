from rest_framework import generics, permissions
from apps.task.models import Task
from apps.task.serializers import TaskListSerializer, TaskCreateSerializer, TaskDetailSerializer


class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (permissions.IsAuthenticated, )


class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)