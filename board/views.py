# board/views.py
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Task
from .serializers import TaskSerializer


@method_decorator(csrf_exempt, name="dispatch")   # ❗ disable CSRF just for this API
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]              # ❗ allow front-end to PATCH without login
