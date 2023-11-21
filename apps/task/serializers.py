from rest_framework import serializers
from apps.task.models import Task


class TaskListSerializer(serializers.ModelSerializer):
    manager_full_name = serializers.SerializerMethodField()
    employee_full_name = serializers.SerializerMethodField()
    device_name = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = ('title', 'manager_full_name', 'employee_full_name', 'device_name')

    def get_manager_full_name(self, obj):
        return obj.manager.full_name if obj.manager else None

    def get_employee_full_name(self, obj):
        return obj.employee.full_name if obj.employee else None

    def get_device_name(self, obj):
        return obj.device.name if obj.device else None


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'