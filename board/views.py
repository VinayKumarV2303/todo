from django.shortcuts import render
from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


# 🧩 Simple view to show your Task Board page
def board_view(request):
    # if your template is at templates/board.html use this:
    return render(request, "board.html")

    # OR if it's at templates/board/board.html then use:
    # return render(request, "board/board.html")


# 🔁 API ViewSet for Tasks
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("due_date", "id")
    serializer_class = TaskSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        assignee = self.request.query_params.get("assignee")
        if assignee:
            qs = qs.filter(assignee=assignee)
        return qs
