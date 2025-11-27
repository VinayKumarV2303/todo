from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("id")
    serializer_class = TaskSerializer

    @action(detail=True, methods=["patch"])
    def update_status(self, request, pk=None):
        task = self.get_object()
        new_status = request.data.get("status")
        if new_status:
            task.status = new_status
            task.save()
            return Response({"success": True})
        return Response({"error": "Invalid status"}, status=400)
