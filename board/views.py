from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Task
from .serializers import TaskSerializer


# 👇 This view just renders your board.html template
def board_page(request):
    return render(request, "board.html")


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint for tasks used by the board.html UI.
    Frontend sends GET /api/tasks/ and PATCH /api/tasks/<id>/
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]  # okay for your internal project
