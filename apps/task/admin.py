from django.contrib import admin
from apps.task.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'manager', 'employee', 'device')
    search_fields = ('title', 'manager', 'employee', 'device')