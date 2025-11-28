from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Task
from .serializers import TaskSerializer


def board_page(request):
    return render(request, "board.html")


@method_decorator(csrf_exempt, name="dispatch")
class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint for tasks used by the board.html UI.

    The frontend:
      - GET   /api/tasks/          (load current state)
      - POST  /api/tasks/          (first click -> create)
      - PATCH /api/tasks/<id>/     (next clicks -> update)
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]  # OK for your internal board
