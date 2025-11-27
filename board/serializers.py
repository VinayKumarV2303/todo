from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "assignee",
            "status",
            "day",  
            "due_date",
            "created_at",
        ]
