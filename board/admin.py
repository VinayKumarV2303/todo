from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "developer", "week", "day", "status")
    list_filter = ("developer", "week", "status")
    search_fields = ("title",)
    ordering = ("developer", "week", "day")
