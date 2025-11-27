from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


def board_view(request):
    # renders templates/board.html
    return render(request, "board.html")


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        developer = self.request.query_params.get("developer")
        if developer:
            qs = qs.filter(developer=developer)
        return qs
