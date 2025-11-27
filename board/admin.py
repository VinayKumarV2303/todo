from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Columns shown in the admin list page
    list_display = ("id", "title", "assignee", "status", "due_date", "created_at")

    # Right-side filter options
    list_filter = ("assignee", "status")

    # Search box
    search_fields = ("title", "description")

    # Default ordering
    ordering = ("assignee", "due_date")
