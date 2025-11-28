from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "assignee", "status", "day")
    list_filter = ("assignee", "status", "day")
    search_fields = ("title",)
    ordering = ("assignee", "day", "title")
