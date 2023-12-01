from rest_framework import serializers
from apps.task.models import Task
from apps.account.models import Account


class TaskListSerializer(serializers.ModelSerializer):
    manager_full_name = serializers.SerializerMethodField()
    employee_full_name = serializers.SerializerMethodField()
    device_name = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'title', 'manager_full_name', 'employee_full_name', 'device_name')

    def get_manager_full_name(self, obj):
        manager = obj.manager
        return manager.full_name if manager and manager.full_name else manager.username if manager and manager.username else manager.id if manager else None

    def get_employee_full_name(self, obj):
        employee = obj.employee
        return employee.full_name if employee and employee.full_name else employee.username if employee and employee.username else employee.id if employee else None

    def get_device_name(self, obj):
        device = obj.device
        return device.name if device else None


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {
            'manager': {'read_only': True}
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        manager = instance.manager
        representation['manager'] = manager.full_name if manager and manager.full_name else manager.username if manager and manager.username else manager.id if manager else None

        employee = instance.employee
        representation['employee'] = employee.full_name if employee and employee.full_name else employee.username if employee and employee.username else employee.id if employee else None

        device = instance.device
        representation['device'] = device.name if device else None

        return representation


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'manager', 'employee', 'device', 'description')
        extra_kwargs = {
            'manager': {'required': False}
        }

    def create(self, validated_data):
        request = self.context.get('request')

        if not request:
            raise serializers.ValidationError("Request object not provided to the serializer context.")

        manager = request.user
        employee = validated_data['employee']
        all_managers = Account.objects.filter(role=0)
        all_employees = Account.objects.filter(role=1)

        if manager not in all_managers:
            raise serializers.ValidationError("You are not allowed to do this action, manager is not found")

        if employee not in all_employees:
            raise serializers.ValidationError("You are not allowed to do this action, employee is not found")

        validated_data['manager'] = manager
        task_instance = Task.objects.create(**validated_data)

        return task_instance
